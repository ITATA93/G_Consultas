# SQLUser.PA_PrDelBabyApgarScore

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PDBAS_ParRef | varchar | PK |  | NO | PA_PregDelBaby Parent Reference |
| PDBAS_ApgarNo | double |  |  | SI | Apgar No |
| PDBAS_Childsub | double |  |  | NO | Childsub |
| PDBAS_Colour | double |  |  | SI | Colour |
| PDBAS_HeartRate | double |  |  | SI | Heart Rate |
| PDBAS_Reflex | double |  |  | SI | Reflex |
| PDBAS_Respiration | double |  |  | SI | Respiration |
| PDBAS_RowId | varchar |  |  | NO | - |
| PDBAS_Tone | double |  |  | SI | Tone |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*