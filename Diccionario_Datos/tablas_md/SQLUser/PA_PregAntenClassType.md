# SQLUser.PA_PregAntenClassType

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ANTCLT_ParRef | bigint | PK |  | NO | PA_Pregnancy Parent Reference |
| ANTCLT_AntenClassType_DR | bigint |  | FK | SI | Des Ref ORCAntenatalClassType |
| ANTCLT_Childsub | double |  |  | NO | Childsub |
| ANTCLT_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*