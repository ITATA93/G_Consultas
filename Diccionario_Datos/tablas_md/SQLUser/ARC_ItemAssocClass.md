# SQLUser.ARC_ItemAssocClass

**Schema:** SQLUser
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ASSOC_ParRef | varchar | PK |  | NO | ARC_ItmMast Parent Reference |
| ASSOC_Childsub | double |  |  | NO | Childsub |
| ASSOC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ASSOC_CreatedDate | date |  |  | SI | Created Date |
| ASSOC_CreatedTime | time |  |  | SI | Created Time |
| ASSOC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ASSOC_DateFrom | date |  |  | NO | Date From |
| ASSOC_DateTo | date |  |  | SI | Date To |
| ASSOC_InsSubCat_DR | varchar |  | FK | SI | Des Ref to ARC_InsSubCat |
| ASSOC_InsType_DR | bigint |  | FK | SI | Des Ref InsuranceType |
| ASSOC_PayorGroup_DR | bigint |  | FK | SI | Des Ref PayorGroup |
| ASSOC_RowId | varchar |  |  | NO | - |
| ASSOC_UpdatedDate | date |  |  | SI | Updated Date |
| ASSOC_UpdatedTime | time |  |  | SI | Updated Time |
| ASSOC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ160DR | - |  |  | SI | Child Reference: Campo Visual (Espec.) |
| Q159Q1 | - |  |  | SI | Uso de Lentes |
| Q159Q2 | - |  |  | SI | Ojo derecho (OD): |
| Q159Q3 | - |  |  | SI | Ojo Izquierdo (OI): |
| Q159Q4 | - |  |  | SI | CAE (OD): |
| Q159Q5 | - |  |  | SI | CAE (OI): |
| Q159Q6 | - |  |  | SI | Comentarios: |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*