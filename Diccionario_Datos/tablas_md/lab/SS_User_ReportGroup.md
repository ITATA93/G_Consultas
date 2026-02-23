# lab.SS_User_ReportGroup

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SURP_ParRef | varchar | PK |  | NO | SS_User Parent Reference |
| SURP_Childsub | double |  |  | NO | Childsub |
| SURP_Destination_DR | varchar |  | FK | SI | Des Ref Print Destination |
| SURP_RepGroup_DR | varchar |  | FK | SI | Des Ref Report Group |
| SURP_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*