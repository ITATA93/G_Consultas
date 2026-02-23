# web_Msg.OIInsertParamsCalTemplate

**Schema:** web_Msg
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| DCTCTUOMDR | bigint |  | FK | SI | Unit Of Measure |
| DCTDurationUnit | varchar |  |  | SI | Duration Unit |
| ID | varchar |  |  | NO | - |
| OID | varchar |  |  | SI | TODO |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| TemplateDR | bigint |  | FK | SI | Template that this is based on |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*