# SQLUser.PA_PregAntenatalCompl

**Schema:** SQLUser
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PANC_ParRef | bigint | PK |  | NO | PA_Pregnancy Parent Reference |
| PANC_Adm_DR | bigint |  | FK | SI | Des Ref PA_Adm |
| PANC_Childsub | double |  |  | NO | Childsub |
| PANC_Complication_DR | bigint |  | FK | SI | Des Ref PAC_PrenatalProblems |
| PANC_RowId | varchar |  |  | NO | - |
| PANC_SortOrder | double |  |  | SI | Sort Order |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*