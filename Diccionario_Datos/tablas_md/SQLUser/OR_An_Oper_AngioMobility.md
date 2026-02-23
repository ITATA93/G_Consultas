# SQLUser.OR_An_Oper_AngioMobility

**Schema:** SQLUser
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Pabellón Quirúrgico**. Gestión de cirugías.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OPAM_ParRef | varchar | PK |  | NO | OR_Anaest_Operation Parent Reference |
| OPAM_Childsub | double |  |  | NO | Childsub |
| OPAM_RowId | varchar |  |  | NO | - |
| OPAM_Type_DR | bigint |  | FK | SI | - |
| Q10Q1 | - |  |  | SI | Treatment |
| Q10Q2 | - |  |  | SI | Other treatment |
| Q10Q3 | - |  |  | SI | Treatment status |
| Q10Q4 | - |  |  | SI | Reason for ceasing |
| Q10Q5 | - |  |  | SI | Other reason for ceasing |
| Q10Q6 | - |  |  | SI | Treatment notes |
| Q10Q7 | - |  |  | SI | Entered by |
| Q10Q8 | - |  |  | SI | Entered date |
| Q10Q9 | - |  |  | SI | Entered time |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*