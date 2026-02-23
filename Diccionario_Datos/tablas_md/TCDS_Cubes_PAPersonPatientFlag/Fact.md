# TCDS_Cubes_PAPersonPatientFlag.Fact

**Schema:** TCDS_Cubes_PAPersonPatientFlag
**Columnas:** 5
**Actualizado:** 2026-01-30 15:31:41

## Utilidad

**TrakCare Data Store**. Almacén de datos para reportería y análisis.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx2709257677 | bigint |  |  | SI | Dimension: Dx2709257677<br/>
Source: FLAGPatientF... |
| DxDSSPatientID | bigint |  |  | SI | Dimension: DxDSSPatientID<br/>
Source: FLAGParRef... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*