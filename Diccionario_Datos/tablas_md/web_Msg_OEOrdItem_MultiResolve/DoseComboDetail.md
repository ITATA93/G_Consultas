# web_Msg_OEOrdItem_MultiResolve.DoseComboDetail

**Schema:** web_Msg_OEOrdItem_MultiResolve
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Detalle de la entidad padre.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| FormStrengthDR | varchar |  | FK | SI | - |
| ID | varchar |  |  | NO | - |
| ParRef | varchar |  |  | SI | - |
| Quantity | double |  |  | SI | - |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| UnitVolumeDR | varchar |  | FK | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*