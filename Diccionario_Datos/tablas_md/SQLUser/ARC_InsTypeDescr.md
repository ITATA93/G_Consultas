# SQLUser.ARC_InsTypeDescr

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Seguros**. Planes y convenios. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DES_ParRef | bigint | PK |  | NO | ARC_InsuranceType Parent Reference |
| ChildQ45DR | - |  |  | SI | Child Reference: Extremidades |
| DES_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| DES_BillGrp_DR | bigint |  | FK | SI | Des Ref BillGrp |
| DES_BillSub_DR | varchar |  | FK | SI | Des Ref BillSub |
| DES_Childsub | double |  |  | NO | Childsub |
| DES_CreatedDate | date |  |  | SI | Created Date |
| DES_CreatedTime | time |  |  | SI | Created Time |
| DES_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DES_Desc | varchar |  |  | SI | Description |
| DES_RowId | varchar |  |  | NO | - |
| DES_UpdatedDate | date |  |  | SI | Updated Date |
| DES_UpdatedTime | time |  |  | SI | Updated Time |
| DES_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q39Q1 | - |  |  | SI | Palpación |
| Q39Q2 | - |  |  | SI | Percusión |
| Q39Q3 | - |  |  | SI | Auscultación |
| Q39Q4 | - |  |  | SI | Localización |
| Q39Q5 | - |  |  | SI | Comentario |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*