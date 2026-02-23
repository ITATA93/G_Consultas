# SQLUser.OR_AnaestMaintenance

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Pabellón Quirúrgico**. Gestión de cirugías.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ANAMN_ParRef | varchar | PK |  | NO | MR_Adm Parent Reference |
| ANAMN_Childsub | double |  |  | NO | Childsub |
| ANAMN_RowId | varchar |  |  | NO | - |
| ANAMN_Type_DR | bigint |  | FK | SI | Des Ref ORCAnaestheticMaintenance |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*