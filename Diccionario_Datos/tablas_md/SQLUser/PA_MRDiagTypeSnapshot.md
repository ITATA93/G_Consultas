# SQLUser.PA_MRDiagTypeSnapshot

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PATYP_ParRef | bigint | PK |  | NO | - |
| PATYP_Childsub | double |  |  | NO | Childsub |
| PATYP_MRCDiagTyp | bigint |  |  | SI | Des Ref to MRCDiagTyp |
| PATYP_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*