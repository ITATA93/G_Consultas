# SQLUser.PA_Process

**Schema:** SQLUser
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PR_RowId | bigint | PK |  | NO | - |
| PR_Billed | varchar |  |  | SI | Billed |
| PR_DRG_DR | bigint |  | FK | SI | Des Ref DRG |
| PR_DateCreation | date |  |  | SI | Date of Creation |
| PR_No | varchar |  |  | SI | Process Number |
| PR_Status | varchar |  |  | SI | Status |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*