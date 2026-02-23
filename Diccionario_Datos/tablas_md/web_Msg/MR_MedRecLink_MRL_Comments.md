# web_Msg.MR_MedRecLink_MRL_Comments

**Schema:** web_Msg
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Medicamentos**. Prescripción y administración de fármacos. Relación entre entidades.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MR_MedRecLink | varchar | PK |  | NO | Parent reference |
| ID | varchar |  |  | NO | - |
| MRL_Comments | varchar |  |  | SI | MRL_Comments |
| element_key | varchar |  |  | NO | MRLComments array key |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*