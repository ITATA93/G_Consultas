# SQLUser.ARC_AuxilInsTypeContractDetails

**Schema:** SQLUser
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CONTR_ParRef | bigint | PK |  | NO | ARC_AuxilInsurType Parent Reference |
| CONTR_CONTR_DR | bigint |  | FK | SI | Des Ref CONTR Det |
| CONTR_Childsub | double |  |  | NO | Childsub |
| CONTR_CreatedDate | date |  |  | SI | Created Date |
| CONTR_CreatedTime | time |  |  | SI | Created Time |
| CONTR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CONTR_DateFrom | date |  |  | NO | Date From |
| CONTR_DateTo | date |  |  | SI | Date To |
| CONTR_RowId | varchar |  |  | NO | - |
| CONTR_UpdatedDate | date |  |  | SI | Updated Date |
| CONTR_UpdatedTime | time |  |  | SI | Updated Time |
| CONTR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q39Q1 | - |  |  | SI | Medicamento (dosis/presentación) |
| Q39Q2 | - |  |  | SI | Estado |
| Q39Q3 | - |  |  | SI | Cantidad |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*