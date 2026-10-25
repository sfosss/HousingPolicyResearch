# Security remediation record

Reviewed: 2026-10-23. Proposed current-document cleanup.

The former incident instructions repeated credential material. The proposed replacement omits those values and keeps the remaining owner actions explicit.

Verified scope: the replacement incident documents contain no historical credential values. No provider credentials were accessed, revoked, rotated or tested. No Git history was rewritten. This is not a complete security assessment of the repository.

Credential-owner follow-up:

1. Privately establish affected providers and exposure periods.
1. Revoke or rotate affected credentials at the provider.
1. Inspect relevant usage records.
1. Review any historical-cleanup plan with the owner and collaborators.

The existing detect-secrets hook remains manual. Required-check enforcement is a separate GitHub settings action and must be verified after saving.
