# websys.TimeZoneRule

**Schema:** websys
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| EffectDay | varchar |  |  | SI | Gives the day on which the rule takes effect.  Rec... |
| EffectMonth | varchar |  |  | SI | Names the month in which the rule takes effect.  M... |
| EffectTime | varchar |  |  | SI | Gives the time of day at which the rule takes effe... |
| Letters | varchar |  |  | SI | Gives the "variable part" (for example, the "S" or... |
| Name | varchar |  |  | SI | Gives the (arbitrary) name of the set of rules thi... |
| Save | varchar |  |  | SI | 	Gives the amount of time to be added to local sta... |
| Type | varchar |  |  | SI | Gives the type of year in which the rule applies. ... |
| YearFrom | varchar |  |  | SI | Gives the first year in which the rule applies.  A... |
| YearTo | varchar |  |  | SI | Gives the final year in which the rule applies.  I... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*