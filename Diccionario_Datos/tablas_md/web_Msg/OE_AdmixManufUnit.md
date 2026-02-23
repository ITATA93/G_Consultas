# web_Msg.OE_AdmixManufUnit

**Schema:** web_Msg
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| UNIT_Childsub | double |  |  | SI | Childsub |
| UNIT_ConditionalPass | varchar |  |  | SI | Conditional Pass  |
| UNIT_Fail | varchar |  |  | SI | Fail   |
| UNIT_ParRef | varchar |  |  | SI | OE_AdmixManuf Parent Reference
Required by User.O... |
| UNIT_Pass | varchar |  |  | SI | Pass  |
| UNIT_RowId | varchar |  |  | SI | - |
| UNIT_UnitNumber | integer |  |  | SI | Unit Number  |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*