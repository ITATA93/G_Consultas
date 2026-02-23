# websys.DSSEventHistory

**Schema:** websys
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Histórico de cambios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| ActionItemDR | varchar |  | FK | SI | - |
| EpisodeDR | bigint |  | FK | SI | - |
| EventDate | date |  |  | SI | - |
| EventTime | time |  |  | SI | - |
| UserDR | bigint |  | FK | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*