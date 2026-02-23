# SQLUser.ARC_ServTaxRate

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RAT_ParRef | bigint | PK |  | NO | ARC_ServTax Parent Reference |
| Q19Q1 | - |  |  | SI | Motivo |
| Q19Q2 | - |  |  | SI | Código |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| RAT_Childsub | double |  |  | NO | Childsub |
| RAT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RAT_CreatedDate | date |  |  | SI | Created Date |
| RAT_CreatedTime | time |  |  | SI | Created Time |
| RAT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RAT_DateFrom | date |  |  | NO | Date From |
| RAT_DateTo | date |  |  | SI | Date To |
| RAT_IPRate | double |  |  | NO | InPatient Rate |
| RAT_IslandRate | double |  |  | SI | Island Rate |
| RAT_OPRate | double |  |  | NO | OutPatient Rate |
| RAT_OrderPriorityRate | double |  |  | SI | Discharge Medication Rate |
| RAT_OrderPriority_DR | bigint |  | FK | SI | Des Ref Discharge Medication |
| RAT_RowId | varchar |  |  | NO | - |
| RAT_UpdatedDate | date |  |  | SI | Updated Date |
| RAT_UpdatedTime | time |  |  | SI | Updated Time |
| RAT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*