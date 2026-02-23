# SQLUser.LBC_ObservationSource

**Schema:** SQLUser
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCOS_ParRef | bigint | PK |  | NO | Parent Procedure |
| LBCOS_Material_DR | bigint |  | FK | SI | Material  |
| LBCOS_RowID | varchar |  |  | NO | - |
| Q54Q1 | - |  |  | SI | Location |
| Q54Q2 | - |  |  | SI | Ulcer grade (University of Texas system) |
| Q54Q3 | - |  |  | SI | Ulcer stage (University of Texas system) |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*