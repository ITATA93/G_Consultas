# web_Msg_OECSchema.EditOEPref

**Schema:** web_Msg_OECSchema
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| AppliedFilter | bit |  |  | SI | Flag to keep track of whether a filter is actually... |
| DisplayDescription | varchar |  |  | SI | - |
| DisplaysByDefault | varchar |  |  | SI | Display by Default; for MEUI, determines whether f... |
| FullDescription | varchar |  |  | SI | - |
| ID | varchar |  |  | NO | - |
| Mandatory | varchar |  |  | SI | Is it mandatory
"Y"|"N"|"" 
if "Y", preference c... |
| OECSchemaDR | bigint |  | FK | SI | - |
| OECSchemaGroupDR | varchar |  | FK | SI | - |
| OrderType | varchar |  |  | SI | - |
| OrderTypeOnly | varchar |  |  | SI | Restrict Item lookup to scheme filter for the Sche... |
| PrefComp | varchar |  |  | NO | - |
| PrefID | varchar |  |  | SI | Preference Identifier - might not be a RowID, work... |
| ReadOnly | bit |  |  | SI | - |
| SchemaOrGroup | integer |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*