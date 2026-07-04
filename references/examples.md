# ecoMode Examples

## Debug

Normal:
> The bug is caused by the authentication middleware attempting to access the
> email property on a user object before verifying that the database lookup
> actually returned a user. If the user does not exist, this results in a null
> reference error. You should add a guard clause after the lookup and return a
> 401 response before accessing the email property.

eco:
> Guard `user` before `.email`; return 401.

## Deploy

Normal:
> To deploy this safely, first make sure that the database migration has been
> applied in staging and that the application has been tested against the new
> schema. After that, deploy the application code, monitor errors, and only then
> remove the old compatibility path.

eco:
> Order: migrate staging, test app, deploy code, monitor errors, remove old path.

## Code Final

eco:
> Done: `src/auth.ts`, `tests/auth.test.ts`.
> Verify: `npm test -- auth` passed.
> Note: 401 path now covers missing user.

## Review

eco:
> `src/payments.ts:88`: high: charge can run twice on retry. Add idempotency key.

## Explanation

eco explain:
> Pooling reuses open DB connections. No per-request handshake. Faster requests, fewer DB connection spikes.

## Question Gate

Ask:
> Which target: installable Codex skill or standalone CLI?

Do not ask:
> What tone should I use?

Infer tone from `ecoMode`: compact, professional.
