# SQLUser.PA_PregPostnatalComp

**Schema:** SQLUser
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PPNC_ParRef | bigint | PK |  | NO | PA_Pregnancy Parent Reference |
| PPNC_Adm_DR | bigint |  | FK | SI | Des Ref PA_Adm |
| PPNC_Childsub | double |  |  | NO | Childsub |
| PPNC_Complication_DR | bigint |  | FK | SI | Des Ref PAC_PostNatalProblems |
| PPNC_RowId | varchar |  |  | NO | - |
| PPNC_SortOrder | double |  |  | SI | Sort Order |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*