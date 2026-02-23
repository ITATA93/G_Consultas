# websys.TimeZone

> "Time Zone

**Schema:** websys
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Format | varchar |  |  | SI | The format for time zone abbreviations in this tim... |
| Name | varchar |  |  | SI | The name of the time zone.  This is the name used ... |
| Offset | varchar |  |  | SI | The amount of time to add to UT to get standard ti... |
| Rule | varchar |  |  | SI | The name of the rule(s) that apply in the time zon... |
| Save | varchar |  |  | SI | An amount of time to add to local standard time.  ... |
| Until | varchar |  |  | SI | The time at which the UT offset or the rule(s) cha... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*