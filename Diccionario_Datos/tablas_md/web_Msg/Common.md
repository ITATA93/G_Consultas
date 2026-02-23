# web_Msg.Common

**Schema:** web_Msg
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ClassName | varchar |  |  | SI | - |
| ID | varchar |  |  | NO | - |
| Lock | bit |  |  | SI | - |
| ReadOnly | bit |  |  | SI | - |
| RowID | varchar |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| Unique | bit |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*