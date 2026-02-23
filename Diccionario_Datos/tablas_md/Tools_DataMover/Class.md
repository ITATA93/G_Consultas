# Tools_DataMover.Class

**Schema:** Tools_DataMover
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Herramientas de Sistema**. Utilidades de administración y carga de datos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| VersionNumber | varchar | PK |  | NO | - |
| ClassName | varchar |  |  | NO | - |
| ID | varchar |  |  | NO | - |
| IsAChildClass | bit |  |  | SI | Indicated if is a child class |
| OtherIdentityClassName | varchar |  |  | SI | - |
| ParRefClassName | varchar |  |  | SI | - |
| ParRefProperty | varchar |  |  | SI | - |
| RowIDGlobalRef | varchar |  |  | SI | Global reference to Row ID |
| RowIDSubscriptCount | integer |  |  | SI | Count of subscripts used for eow ID global referen... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*