# web_Msg.Document

**Schema:** web_Msg
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| Comments | varchar |  |  | SI | Comments |
| Data | longvarbinary |  |  | SI | Document data |
| DataId | varchar |  |  | SI | Id of the foreign data global (eg ^websys.Document... |
| DataType | varchar |  |  | SI | Name of the foreign data global (eg TIF) |
| ID | varchar |  |  | NO | - |
| Name | varchar |  |  | SI | Document name |
| ReadOnly | bit |  |  | SI | - |
| RowID | varchar |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| Type | varchar |  |  | SI | Document type |
| childsub | bigint |  |  | NO | - |
| docType | varchar |  |  | SI | extension of attachment |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*