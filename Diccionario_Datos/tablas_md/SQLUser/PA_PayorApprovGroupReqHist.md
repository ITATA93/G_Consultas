# SQLUser.PA_PayorApprovGroupReqHist

**Schema:** SQLUser
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAPPGRPREQH_RowId | bigint | PK |  | NO | - |
| PAPPGRPREQH_ApprGroupRequest_DR | bigint |  | FK | SI | Des Ref PAPayorApprovalGroupRequest |
| PAPPGRPREQH_ApprovRequests | varchar |  |  | SI | Des Ref PAPayorApprovalRequest |
| PAPPGRPREQH_UpdateDate | date |  |  | SI | Update Date |
| PAPPGRPREQH_UpdateTime | time |  |  | SI | Update Time |
| PAPPGRPREQH_UpdateUser_DR | bigint |  | FK | SI | Des Ref SSUser |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*