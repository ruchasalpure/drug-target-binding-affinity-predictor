# Multi-Agent Coordination Specification

## Assigned Roles
Maker:
binding-affinity-estimator

Checker:
steric-clash-checker

## Coordination Protocol
- **Primary Agent**: drug-target-binding-affinity-predictor
- **Governance Standard**: OpenGAP Dual-Agent Control Framework v0.1.0
- **Consensus Threshold**: 100% agreement between Maker and Checker before state mutations.
- **Fail-safe Mode**: If verification fails, transaction rolls back and alerts human supervisor.
