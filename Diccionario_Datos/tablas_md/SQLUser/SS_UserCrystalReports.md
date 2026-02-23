# SQLUser.SS_UserCrystalReports

**Schema:** SQLUser
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CRYST_ParRef | bigint | PK |  | NO | SS_User Parent Reference |
| CRYST_Childsub | double |  |  | NO | Childsub |
| CRYST_CrystalReportName | varchar |  |  | SI | Crystal Report Name |
| CRYST_ObjectReference | varchar |  |  | SI | ActiveX Object Reference |
| CRYST_PrintPreview | varchar |  |  | SI | Print Preview |
| CRYST_PromptForParameters | varchar |  |  | SI | Prompt For Parameters |
| CRYST_Report_DR | varchar |  | FK | SI | Des Ref Report |
| CRYST_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*