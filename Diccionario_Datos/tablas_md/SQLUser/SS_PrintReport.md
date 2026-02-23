# SQLUser.SS_PrintReport

**Schema:** SQLUser
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PR_RowId | bigint | PK |  | NO | - |
| PR_Content | varchar |  |  | SI | Content |
| PR_Date | date |  |  | SI | Date |
| PR_Days | double |  |  | SI | Days |
| PR_DispensedFlag | varchar |  |  | SI | Dispensed Flag |
| PR_ReportType | varchar |  |  | SI | Report Type |
| PR_Report_DR | bigint |  | FK | SI | Des Ref Report_DR |
| PR_Time | time |  |  | SI | Time |
| PR_User_DR | bigint |  | FK | SI | Des Ref User |
| PR_Ward_DR | bigint |  | FK | SI | Des Ref Ward |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*