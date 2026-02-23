# web_Msg_OEOrdItem_MultiResolve.Form

**Schema:** web_Msg_OEOrdItem_MultiResolve
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| FormDR | bigint |  | FK | SI | - |
| ID | varchar |  |  | NO | - |
| ReadOnly | bit |  |  | SI | - |
| Selected | varchar |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*