# epr.FPView

**Schema:** epr
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**EPR - Registro Electrónico de Pacientes**. Módulo de ficha clínica electrónica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| FPVCode | varchar |  |  | SI | - |
| FPVDesc | varchar |  |  | SI | - |
| FPVHeight | integer |  |  | SI | - |
| FPVIgnoteTempLoc | bit |  |  | SI | - |
| FPVItem | varchar |  |  | SI | - |
| FPVLayout | varchar |  |  | SI | Name of the layout linked to the view in Mobile En... |
| FPVMainView | bit |  |  | SI | - |
| FPVViewLinkedRooms | bit |  |  | SI | - |
| FPVViewNextMostUrgent | bit |  |  | SI | - |
| FPVWard | bigint |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*