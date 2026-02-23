# SQLUser.SS_SecurityOverride

**Schema:** SQLUser
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SECOV_RowId | bigint | PK |  | NO | - |
| SECOV_AccessProfileFrom_DR | bigint |  | FK | SI | Access Profile From |
| SECOV_AccessProfileTo_DR | bigint |  | FK | SI | Access Profile To |
| SECOV_AuthoriseClinician_DR | varchar |  | FK | SI | Des Ref AuthoriseClinician |
| SECOV_BreakTheGlassReason_DR | bigint |  | FK | SI | Des ref to Reason for Break the Glass code table |
| SECOV_Comments | varchar |  |  | SI | Comments |
| SECOV_Date | date |  |  | SI | Date |
| SECOV_OverseeUser_DR | bigint |  | FK | SI | Des Ref OverseeUser |
| SECOV_PatientConsented | varchar |  |  | SI | Patient consent flag |
| SECOV_Patient_DR | bigint |  | FK | SI | Des Ref Patient |
| SECOV_Reason | varchar |  |  | SI | Reason  |
| SECOV_ReferenceNumber | varchar |  |  | SI | Reference Number |
| SECOV_SecurityGroupFrom_DR | bigint |  | FK | SI | Des Ref SSGroup |
| SECOV_SecurityGroupTo_DR | bigint |  | FK | SI | Des Ref SSGroup |
| SECOV_Time | time |  |  | SI | Time |
| SECOV_User_DR | bigint |  | FK | SI | Des Ref User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*