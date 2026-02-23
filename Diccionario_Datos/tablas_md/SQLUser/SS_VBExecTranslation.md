# SQLUser.SS_VBExecTranslation

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EXTR_ParRef | bigint | PK |  | NO | SS_VBExecutables Parent Reference |
| EXTR_Desc | varchar |  |  | NO | Translation |
| EXTR_RowId | varchar |  |  | NO | - |
| EXTR_SSLAN_DR | bigint |  | FK | NO | Des Ref to SSLAN |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*