# Deployment Guide

## Overview

This guide covers the deployment process for company applications across development, staging, and production environments.

## Environments

### Development Environment
- **Purpose**: Local development and testing
- **URL**: dev.company.com
- **Database**: dev-db.company.com
- **Access**: VPN required for remote access
- **Data**: Sample/test data only

### Staging Environment
- **Purpose**: Pre-production testing and QA
- **URL**: staging.company.com
- **Database**: staging-db.company.com
- **Access**: VPN required
- **Data**: Near-production data (sanitized)

### Production Environment
- **Purpose**: Live customer-facing applications
- **URL**: app.company.com
- **Database**: prod-db.company.com
- **Access**: Strict access control
- **Data**: Real customer data

## Prerequisites

### Required Tools
- Docker 20.10+
- Docker Compose 2.0+
- kubectl (for Kubernetes deployments)
- Git 2.30+
- AWS CLI (for cloud deployments)
- Company VPN client

### Access Requirements
- VPN connection for all environments
- SSH access to servers
- Database credentials (from password manager)
- API tokens (from IT portal)

### Security Clearance
- Development: All developers
- Staging: Developers + QA team
- Production: DevOps team only (with manager approval)

## Deployment Process

### Development Deployment

#### Local Development
```bash
# Clone repository
git clone https://github.com/company/app.git
cd app

# Install dependencies
npm install

# Set environment variables
cp .env.example .env
# Edit .env with your settings

# Run locally
npm run dev
```

#### Development Server
```bash
# Build Docker image
docker build -t company/app:dev .

# Push to development registry
docker push company/app:dev

# Deploy to development server
kubectl apply -f k8s/dev-deployment.yaml
```

### Staging Deployment

#### Pre-Deployment Checklist
- [ ] All tests passing in CI/CD
- [ ] Code review approved
- [ ] Migration scripts tested
- [ ] Configuration files updated
- [ ] Staging database backed up
- [ ] Rollback plan documented

#### Deployment Steps
```bash
# 1. Create feature branch from main
git checkout -b feature/deploy-to-staging

# 2. Update version
npm version patch

# 3. Build production-ready image
docker build -t company/app:staging-latest .

# 4. Run integration tests
npm run test:integration

# 5. Push to staging registry
docker push company/app:staging-latest

# 6. Deploy to staging
kubectl apply -f k8s/staging-deployment.yaml

# 7. Verify deployment
kubectl rollout status deployment/app-staging

# 8. Run smoke tests
npm run test:smoke -- --env=staging
```

#### Verification
- Check application health: `https://staging.company.com/health`
- Verify database migrations
- Test critical user flows
- Monitor logs for errors

### Production Deployment

#### Pre-Deployment Requirements
- Manager approval required
- Scheduled maintenance window
- Production database backed up
- Rollback plan approved
- On-call engineer assigned

#### Deployment Steps
```bash
# 1. Schedule deployment in deployment calendar
# Contact DevOps team at least 48 hours in advance

# 2. Create release branch
git checkout -b release/v1.2.3

# 3. Update version
npm version minor

# 4. Tag release
git tag -a v1.2.3 -m "Release version 1.2.3"
git push origin v1.2.3

# 5. Build production image
docker build -t company/app:1.2.3 .

# 6. Run full test suite
npm run test:all

# 7. Push to production registry
docker push company/app:1.2.3

# 8. Deploy to production (blue-green deployment)
kubectl apply -f k8s/prod-deployment.yaml

# 9. Monitor rollout
kubectl rollout status deployment/app-prod

# 10. Verify production
curl https://app.company.com/health
```

#### Post-Deployment
- Monitor application metrics
- Check error rates
- Verify database performance
- Notify stakeholders of successful deployment
- Update deployment documentation

## Database Migrations

### Migration Process
```bash
# Create new migration
npm run migration:create --name=add_user_preferences

# Run migration on development
npm run migration:up --env=dev

# Test migration on staging
npm run migration:up --env=staging

# Rollback if needed
npm run migration:down --env=staging

# Run on production (during maintenance window)
npm run migration:up --env=prod
```

### Migration Best Practices
- Always test migrations on staging first
- Create rollback scripts for all migrations
- Never modify existing migrations
- Use transactions for data changes
- Back up tables before schema changes

## Rollback Procedures

### Application Rollback
```bash
# Quick rollback to previous version
kubectl rollout undo deployment/app-prod

# Rollback to specific version
kubectl rollout undo deployment/app-prod --to-revision=3

# Verify rollback
kubectl rollout status deployment/app-prod
```

### Database Rollback
```bash
# Rollback last migration
npm run migration:down --env=prod

# Rollback to specific migration
npm run migration:down --env=prod --to=20240101000000

# Restore from backup (if needed)
# Contact DBA team for backup restoration
```

## Monitoring

### Application Monitoring
- **Metrics**: CPU, memory, response time, error rate
- **Tools**: Prometheus, Grafana
- **Alerts**: PagerDuty for critical issues
- **Dashboard**: monitoring.company.com

### Log Monitoring
- **Centralized Logging**: ELK Stack
- **Log Levels**: ERROR, WARN, INFO, DEBUG
- **Retention**: 30 days for production
- **Access**: logs.company.com

### Database Monitoring
- **Performance**: Query times, connection pool
- **Replication**: Lag, sync status
- **Storage**: Disk usage, growth rate
- **Alerts**: DBA team notified for issues

## Troubleshooting

### Deployment Failures

**Image Pull Errors**
```bash
# Check image exists
docker pull company/app:1.2.3

# Check registry authentication
docker login registry.company.com

# Verify image tag
docker images | grep company/app
```

**Pod Not Starting**
```bash
# Check pod status
kubectl get pods -n production

# Check pod logs
kubectl logs <pod-name> -n production

# Describe pod for events
kubectl describe pod <pod-name> -n production
```

**Health Check Failures**
```bash
# Check health endpoint
curl https://app.company.com/health

# Check service status
kubectl get svc -n production

# Check ingress configuration
kubectl get ingress -n production
```

### Performance Issues

**High CPU Usage**
```bash
# Check resource usage
kubectl top pods -n production

# Check HPA status
kubectl get hpa -n production

# Scale up if needed
kubectl scale deployment app-prod --replicas=4
```

**High Memory Usage**
```bash
# Check memory limits
kubectl describe deployment app-prod

# Check pod memory
kubectl top pods -n production --containers

# Adjust limits in deployment YAML
```

## Security

### Secrets Management
- Use Kubernetes Secrets for sensitive data
- Never commit secrets to Git
- Rotate secrets quarterly
- Use company secret manager

### Access Control
- RBAC for Kubernetes access
- IAM roles for AWS resources
- VPN required for all access
- MFA enabled for all accounts

### Compliance
- SOC 2 compliance requirements
- Data encryption at rest and in transit
- Regular security audits
- Penetration testing quarterly

## CI/CD Pipeline

### Pipeline Stages
1. **Build**: Compile and package application
2. **Test**: Run unit and integration tests
3. **Security Scan**: Check for vulnerabilities
4. **Deploy to Dev**: Automatic on merge to develop
5. **Deploy to Staging**: Manual approval required
6. **Deploy to Production**: Manager approval required

### Pipeline Triggers
- Push to develop branch → Dev deployment
- Pull request to main → Staging deployment
- Tagged release → Production deployment

## Best Practices

### Code Quality
- Write unit tests for all new code
- Maintain test coverage above 80%
- Use linters and formatters
- Conduct code reviews

### Documentation
- Update README for new features
- Document API changes
- Maintain CHANGELOG
- Update deployment guides

### Communication
- Notify team of deployments
- Schedule production deployments
- Document incidents
- Share lessons learned

## Emergency Procedures

### Critical Bug in Production
1. Immediately notify on-call engineer
2. Assess impact and severity
3. Implement quick fix if possible
4. Rollback if fix is not feasible
5. Schedule proper fix for next release
6. Conduct post-mortem

### Database Outage
1. Contact DBA team immediately
2. Switch to read replica if available
3. Enable maintenance mode
4. Restore from backup if needed
5. Verify data integrity
6. Resume operations

### Security Incident
1. Immediately notify security team
2. Isolate affected systems
3. Preserve evidence
4. Follow incident response plan
5. Communicate with stakeholders
6. Conduct post-incident review

## Contact Information

### DevOps Team
- Email: devops@company.com
- Slack: #devops
- On-call: 555-0199 (24/7)

### DBA Team
- Email: dba@company.com
- Slack: #database
- On-call: 555-0200 (24/7)

### Security Team
- Email: security@company.com
- Slack: #security
- Emergency: 555-0198 (24/7)

---

Last updated: April 2024
