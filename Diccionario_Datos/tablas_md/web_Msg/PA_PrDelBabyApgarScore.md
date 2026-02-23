# web_Msg.PA_PrDelBabyApgarScore

**Schema:** web_Msg
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ApgarLookupTotal | double |  |  | SI | ApgarLookupTotal |
| ApgarMin | double |  |  | SI | ApgarMin |
| ID | varchar |  |  | NO | - |
| PDBAS_ApgarNo | double |  |  | SI | Apgar No |
| PDBAS_Childsub | double |  |  | SI | Childsub |
| PDBAS_Colour | double |  |  | SI | Colour |
| PDBAS_HeartRate | double |  |  | SI | Heart Rate |
| PDBAS_ParRef | varchar |  |  | SI | PA_PregDelBaby Parent Reference
Required by User.... |
| PDBAS_Reflex | double |  |  | SI | Reflex |
| PDBAS_Respiration | double |  |  | SI | Respiration |
| PDBAS_RowId | varchar |  |  | SI | - |
| PDBAS_Tone | double |  |  | SI | Tone |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*