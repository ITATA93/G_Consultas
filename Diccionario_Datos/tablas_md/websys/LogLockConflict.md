# websys.LogLockConflict

> Record of any encountered websys.Lock conflicts

**Schema:** websys
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Registro de eventos.

*Descripción original:* Record of any encountered websys.Lock conflicts

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| ConflictDate | date |  |  | SI | The date of the lock conflict |
| ConflictTime | time |  |  | SI | The time of the lock conflict |
| LockAttemptClassName | varchar |  |  | SI | Class name of the record that was attempted to be ... |
| LockAttemptComponentName | varchar |  |  | SI | Component on which the lock was attempted
***NOTE... |
| LockAttemptId | varchar |  |  | SI | ID of the record that was attempted to be locked |
| LockAttemptLogonLocationDR | bigint |  | FK | SI | Logon location of the user that attempted to lock ... |
| LockAttemptSecurityGroupDR | bigint |  | FK | SI | Security group  of the user that attempted to lock... |
| LockAttemptSessionId | varchar |  |  | SI | Session ID of the user that attempted to lock the ... |
| LockAttemptUserDR | bigint |  | FK | SI | The user that attempted to lock the record |
| LockedClassName | varchar |  |  | SI | Class name of the record that was locked |
| LockedComponentName | varchar |  |  | SI | Last component name where the lock was taken.
***... |
| LockedId | varchar |  |  | SI | ID of the record that was locked |
| LockedLogonLocationDR | bigint |  | FK | SI | Logon Location of the user that had originally loc... |
| LockedSessionId | varchar |  |  | SI | Session ID of the user that had originally locked ... |
| LockedUserDR | bigint |  | FK | SI | User that had originally locked the record |
| Message | varchar |  |  | SI | The message from websys.Lock:Lock method that was ... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*