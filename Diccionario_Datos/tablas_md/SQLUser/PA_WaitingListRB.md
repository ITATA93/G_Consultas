# SQLUser.PA_WaitingListRB

**Schema:** SQLUser
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Lista de Espera**. Gestión de pacientes en espera.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RB_ParRef | bigint | PK |  | NO | PA_WaitingList Parent Reference |
| RB_AuxInsType_DR | bigint |  | FK | SI | Des Ref AuxInsType |
| RB_CTLOC_DR | bigint |  | FK | SI | Des Ref Booking Dep |
| RB_Childsub | double |  |  | NO | Childsub |
| RB_InsType_DR | bigint |  | FK | SI | Des Ref InsType |
| RB_OEORI_DR | varchar |  | FK | SI | Des Ref OEORI |
| RB_RowId | varchar |  |  | NO | - |
| RB_ServiceKey | varchar |  |  | SI | ServiceKey |
| RB_Service_DR | bigint |  | FK | SI | Des Ref Service |
| RB_Status_DR | bigint |  | FK | SI | Des Ref Status |
| RB_Type_DR | bigint |  | FK | SI | Des REf WLType |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*