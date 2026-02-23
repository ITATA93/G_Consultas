# epr.CTDietType

**Schema:** epr
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Active | varchar |  |  | SI | - |
| CTHospDR | bigint |  | FK | SI | - |
| CTLocDR | bigint |  | FK | SI | - |
| Code | varchar |  |  | SI | - |
| Cycles | varchar |  |  | SI | - |
| DateFrom | date |  |  | SI | - |
| Description | varchar |  |  | SI | - |
| FirstCycleSttDate | date |  |  | SI | - |
| LenOfCycle | integer |  |  | SI | - |
| NumOfCycles | integer |  |  | SI | - |
| OrigMealType | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*