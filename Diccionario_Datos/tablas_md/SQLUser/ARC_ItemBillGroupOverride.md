# SQLUser.ARC_ItemBillGroupOverride

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BILLGRP_ParRef | varchar | PK |  | NO | ARC_ItmMast Parent Reference |
| BILLGRP_BillGrp_DR | bigint |  | FK | SI | Des Ref ARCBillGrp |
| BILLGRP_BillSub_DR | varchar |  | FK | SI | Des Ref ARCBillSub |
| BILLGRP_Childsub | double |  |  | NO | Childsub |
| BILLGRP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| BILLGRP_CreatedDate | date |  |  | SI | Created Date |
| BILLGRP_CreatedTime | time |  |  | SI | Created Time |
| BILLGRP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| BILLGRP_DateFrom | date |  |  | NO | Date From |
| BILLGRP_DateTo | date |  |  | SI | Date To |
| BILLGRP_InsType_DR | bigint |  | FK | SI | Des Ref InsType |
| BILLGRP_RowId | varchar |  |  | NO | - |
| BILLGRP_UpdatedDate | date |  |  | SI | Updated Date |
| BILLGRP_UpdatedTime | time |  |  | SI | Updated Time |
| BILLGRP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ162DR | - |  |  | SI | Child Reference: Otras evaluaciones del Nervio Ópt... |
| Q160Q1 | - |  |  | SI | Ojos |
| Q160Q2 | - |  |  | SI | Evaluación |
| Q160Q3 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*