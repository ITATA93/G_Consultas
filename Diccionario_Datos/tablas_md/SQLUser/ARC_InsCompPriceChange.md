# SQLUser.ARC_InsCompPriceChange

**Schema:** SQLUser
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Seguros**. Planes y convenios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INSPR_RowId | bigint | PK |  | NO | - |
| ChildQ65DR | - |  |  | SI | Child Reference: Extremidades |
| INSPR_CreatedDate | date |  |  | SI | Created Date |
| INSPR_CreatedTime | time |  |  | SI | Created Time |
| INSPR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INSPR_Date | date |  |  | NO | Effective Date |
| INSPR_InsType_DR | bigint |  | FK | SI | Des Ref InsType |
| INSPR_UpdatedDate | date |  |  | SI | Updated Date |
| INSPR_UpdatedTime | time |  |  | SI | Updated Time |
| INSPR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q58Q1 | - |  |  | SI | Palpación |
| Q58Q2 | - |  |  | SI | Percusión |
| Q58Q3 | - |  |  | SI | Auscultación |
| Q58Q4 | - |  |  | SI | Localización |
| Q58Q5 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*