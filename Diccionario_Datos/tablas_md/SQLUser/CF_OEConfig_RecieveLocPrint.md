# SQLUser.CF_OEConfig_RecieveLocPrint

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Configuración del módulo.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LOC_ParRef | bigint | PK |  | NO | CF_OEConfig Parent Reference |
| LOC_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| LOC_Childsub | double |  |  | NO | Childsub |
| LOC_RowId | varchar |  |  | NO | - |
| Q88Q1 | - |  |  | SI | Lateralidad |
| Q88Q2 | - |  |  | SI | Extremidad |
| Q88Q3 | - |  |  | SI | Especificación |
| Q88Q4 | - |  |  | SI | Fecha |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*