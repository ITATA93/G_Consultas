# SQLUser.PA_PrDelBabyResusMthd

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PDBRM_ParRef | varchar | PK |  | NO | PA_PregDelBaby Parent Reference |
| PDBRM_Childsub | double |  |  | NO | Childsub |
| PDBRM_ResusMthd_DR | bigint |  | FK | SI | Des Ref PAC_ResusMethods |
| PDBRM_RowId | varchar |  |  | NO | - |
| PDBRM_SortOrder | double |  |  | SI | Sort Order |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*