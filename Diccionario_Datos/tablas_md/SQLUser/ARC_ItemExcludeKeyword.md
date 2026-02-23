# SQLUser.ARC_ItemExcludeKeyword

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EXCL_RowId | bigint | PK |  | NO | - |
| EXCL_CreatedDate | date |  |  | SI | Created Date |
| EXCL_CreatedTime | time |  |  | SI | Created Time |
| EXCL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| EXCL_Text | varchar |  |  | SI | Text |
| EXCL_UpdatedDate | date |  |  | SI | Updated Date |
| EXCL_UpdatedTime | time |  |  | SI | Updated Time |
| EXCL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q03Q1 | - |  |  | SI | Date entered |
| Q03Q2 | - |  |  | SI | Time entered |
| Q03Q3 | - |  |  | SI | Treatment |
| Q03Q4 | - |  |  | SI | Other treatment |
| Q03Q5 | - |  |  | SI | Treatment status |
| Q03Q6 | - |  |  | SI | Reason for cessation |
| Q03Q7 | - |  |  | SI | Other reason for cessation |
| Q03Q8 | - |  |  | SI | Treatment notes |
| Q03Q9 | - |  |  | SI | Entered by |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*