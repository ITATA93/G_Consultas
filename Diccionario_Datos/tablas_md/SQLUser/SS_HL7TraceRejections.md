# SQLUser.SS_HL7TraceRejections

**Schema:** SQLUser
**Columnas:** 3
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HL7TR_ParRef | varchar | PK |  | NO | SS_HL7Trace Parent Reference |
| HL7TR_Rej_DR | bigint |  | FK | NO | Des Ref to OE_HL7Messages |
| HL7TR_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*