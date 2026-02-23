# web_Msg.MR_Medication_MED_Details

**Schema:** web_Msg
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Medicamentos**. Prescripción y administración de fármacos. Detalle de la entidad padre.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MR_Medication | varchar | PK |  | NO | Parent reference |
| ID | varchar |  |  | NO | - |
| MED_Details | varchar |  |  | SI | MED_Details |
| element_key | varchar |  |  | NO | MEDDetails array key |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*