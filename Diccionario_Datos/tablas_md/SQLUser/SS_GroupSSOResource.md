# SQLUser.SS_GroupSSOResource

**Schema:** SQLUser
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SSOR_ParRef | bigint | PK |  | NO | SS_Group Parent Reference |
| SSOR_Childsub | double |  |  | NO | Childsub |
| SSOR_DateFrom | date |  |  | SI | Date From |
| SSOR_DateTo | date |  |  | SI | Date To |
| SSOR_RowId | varchar |  |  | NO | - |
| SSOR_SingleSignOnRes_DR | bigint |  | FK | SI | Des Ref SSSingleSignOnResource |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*