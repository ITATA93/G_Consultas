# web_Msg.MR_AdmMedicationHistory_MEDHIST_Comments

**Schema:** web_Msg
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Histórico de cambios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MR_AdmMedicationHistory | varchar | PK |  | NO | Parent reference |
| ID | varchar |  |  | NO | - |
| MEDHIST_Comments | varchar |  |  | SI | MEDHIST_Comments |
| element_key | varchar |  |  | NO | MEDHISTComments array key |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*