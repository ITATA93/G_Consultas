# SQLUser.ARC_ItemBillingItem

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ARCIBI_ParRef | varchar | PK |  | NO | ARC_ItmMast Parent Reference |
| ARCIBI_BillingItem_DR | bigint |  | FK | NO | Billing Item |
| ARCIBI_Childsub | double |  |  | NO | Childsub |
| ARCIBI_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ARCIBI_CreatedDate | date |  |  | SI | Created Date |
| ARCIBI_CreatedTime | time |  |  | SI | Created Time |
| ARCIBI_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ARCIBI_DateFrom | date |  |  | SI | Date From |
| ARCIBI_DateTo | date |  |  | SI | Date To |
| ARCIBI_InvoiceDescription | varchar |  |  | SI | Invoice Description |
| ARCIBI_Quantity | integer |  |  | SI | Quantity |
| ARCIBI_RowId | varchar |  |  | NO | - |
| ARCIBI_UpdatedDate | date |  |  | SI | Updated Date |
| ARCIBI_UpdatedTime | time |  |  | SI | Updated Time |
| ARCIBI_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ166DR | - |  |  | SI | Child Reference: Pupila: Defecto Pupilar Aferente ... |
| Q162Q1 | - |  |  | SI | Area |
| Q162Q2 | - |  |  | SI | Ojo derecho (OD): |
| Q162Q3 | - |  |  | SI | Ojo Izquierdo (OI): |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*