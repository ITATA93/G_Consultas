# SQLUser.SS_GroupSSOActivity

**Schema:** SQLUser
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SSOA_ParRef | bigint | PK |  | NO | SS_Group Parent Reference |
| SSOA_Childsub | double |  |  | NO | Childsub |
| SSOA_DateFrom | date |  |  | SI | Date From |
| SSOA_DateTo | date |  |  | SI | Date To |
| SSOA_RowId | varchar |  |  | NO | - |
| SSOA_SingleSignOnActivity_DR | bigint |  | FK | SI | Des Ref SSSingleSignOnActivity |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*