# SQLUser.OR_AnaestMonOtherTechnique

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Pabellón Quirúrgico**. Gestión de cirugías.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ANAMTECH_Childsub | double | PK |  | NO | Childsub |
| ANAMTECH_ParRef | varchar | PK |  | NO | MR_Adm Parent Reference |
| ANAMTECH_RowId | varchar | PK |  | NO | - |
| ANAMTECH_Type_DR | bigint | PK | FK | SI | Des Ref ORCOtherAnaestheticTechniques |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*