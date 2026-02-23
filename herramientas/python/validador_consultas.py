#!/usr/bin/env python3
"""
Validador de Consultas SQL - TrakCare/ALMA
==========================================

Sistema de seguridad para validar consultas SQL antes de ejecutarlas
en la base de datos TrakCare/ALMA.

GARANTIZA:
- Solo consultas SELECT
- Límite de registros (TOP N)
- WHERE en tablas grandes
- No comandos destructivos

Autor: Sistema de Mapeo TrakCare
Fecha: 2026-01-25
"""

import re
from typing import Tuple, List, Dict
from dataclasses import dataclass

@dataclass
class ValidationResult:
    """Resultado de validación de consulta"""
    is_valid: bool
    errors: List[str]
    warnings: List[str]
    suggestions: List[str]

class SQLValidator:
    """Validador de consultas SQL para TrakCare/ALMA"""

    # Configuración de límites
    MAX_ROWS = 1000
    DEFAULT_ROWS = 100
    MAX_TIMEOUT = 30

    # Comandos prohibidos
    FORBIDDEN_COMMANDS = [
        'UPDATE', 'DELETE', 'INSERT', 'DROP', 'TRUNCATE',
        'ALTER', 'CREATE', 'GRANT', 'REVOKE', 'EXEC',
        'EXECUTE', 'MERGE', 'REPLACE'
    ]

    # Tablas grandes que requieren WHERE obligatorio
    LARGE_TABLES = [
        'PA_Adm', 'PA_PatMas', 'PA_Person',
        'MR_Adm', 'MR_Diagnos',
        'OE_Order', 'OE_OrdItem',
        'LB_Result', 'ARC_ItmMast'
    ]

    def __init__(self):
        self.errors = []
        self.warnings = []
        self.suggestions = []

    def validate(self, sql: str) -> ValidationResult:
        """
        Valida una consulta SQL completa

        Args:
            sql: Consulta SQL a validar

        Returns:
            ValidationResult con errores, warnings y sugerencias
        """
        self.errors = []
        self.warnings = []
        self.suggestions = []

        # Limpiar y normalizar SQL
        sql_clean = self._clean_sql(sql)
        sql_upper = sql_clean.upper()

        # Validaciones críticas (errores)
        self._check_forbidden_commands(sql_upper)
        self._check_only_select(sql_upper)
        self._check_has_limit(sql_clean)
        self._check_limit_value(sql_clean)

        # Validaciones de optimización (warnings)
        self._check_select_star(sql_upper)
        self._check_large_tables_without_where(sql_clean, sql_upper)

        # Sugerencias de mejora
        self._add_suggestions(sql_clean)

        is_valid = len(self.errors) == 0

        return ValidationResult(
            is_valid=is_valid,
            errors=self.errors,
            warnings=self.warnings,
            suggestions=self.suggestions
        )

    def _clean_sql(self, sql: str) -> str:
        """Limpia comentarios y espacios extra del SQL"""
        # Eliminar comentarios de línea
        sql = re.sub(r'--[^\n]*', '', sql)
        # Eliminar comentarios de bloque
        sql = re.sub(r'/\*.*?\*/', '', sql, flags=re.DOTALL)
        # Normalizar espacios
        sql = ' '.join(sql.split())
        return sql.strip()

    def _check_forbidden_commands(self, sql_upper: str):
        """Verifica que no haya comandos prohibidos"""
        for cmd in self.FORBIDDEN_COMMANDS:
            if re.search(r'\b' + cmd + r'\b', sql_upper):
                self.errors.append(
                    f"⛔ PROHIBIDO: Comando '{cmd}' no permitido. "
                    f"Solo se permiten consultas SELECT de lectura."
                )

    def _check_only_select(self, sql_upper: str):
        """Verifica que sea una consulta SELECT"""
        # Buscar el primer comando SQL (ignorando WITH, comentarios, etc.)
        match = re.search(r'\b(SELECT|UPDATE|DELETE|INSERT|DROP|ALTER|CREATE)\b', sql_upper)
        if match:
            first_cmd = match.group(1)
            if first_cmd != 'SELECT':
                self.errors.append(
                    f"⛔ PROHIBIDO: Solo se permiten consultas SELECT. "
                    f"Detectado: {first_cmd}"
                )
        else:
            self.errors.append(
                "⛔ ERROR: No se detectó ningún comando SQL válido."
            )

    def _check_has_limit(self, sql: str):
        """Verifica que la consulta tenga límite TOP N"""
        sql_upper = sql.upper()

        # Buscar TOP N
        has_top = re.search(r'\bTOP\s+\d+\b', sql_upper)

        # Buscar LIMIT N (aunque IRIS usa TOP)
        has_limit = re.search(r'\bLIMIT\s+\d+\b', sql_upper)

        if not (has_top or has_limit):
            self.errors.append(
                f"⛔ OBLIGATORIO: La consulta DEBE tener TOP N (máximo {self.MAX_ROWS}). "
                f"Ejemplo: SELECT TOP {self.DEFAULT_ROWS} ..."
            )

    def _check_limit_value(self, sql: str):
        """Verifica que el límite no exceda el máximo permitido"""
        sql_upper = sql.upper()

        # Buscar valor de TOP
        match = re.search(r'\bTOP\s+(\d+)\b', sql_upper)
        if match:
            limit_value = int(match.group(1))
            if limit_value > self.MAX_ROWS:
                self.errors.append(
                    f"⛔ LÍMITE EXCEDIDO: TOP {limit_value} supera el máximo permitido "
                    f"de {self.MAX_ROWS} registros."
                )
            elif limit_value < 1:
                self.errors.append(
                    f"⛔ LÍMITE INVÁLIDO: TOP {limit_value} debe ser mayor a 0."
                )

        # Buscar valor de LIMIT
        match = re.search(r'\bLIMIT\s+(\d+)\b', sql_upper)
        if match:
            limit_value = int(match.group(1))
            if limit_value > self.MAX_ROWS:
                self.errors.append(
                    f"⛔ LÍMITE EXCEDIDO: LIMIT {limit_value} supera el máximo permitido "
                    f"de {self.MAX_ROWS} registros."
                )

    def _check_select_star(self, sql_upper: str):
        """Advierte sobre uso de SELECT *"""
        if re.search(r'\bSELECT\s+\*\b', sql_upper):
            self.warnings.append(
                "⚠️ OPTIMIZACIÓN: Evita SELECT *. Especifica las columnas necesarias "
                "para mejorar el rendimiento."
            )

    def _check_large_tables_without_where(self, sql: str, sql_upper: str):
        """Verifica que tablas grandes tengan cláusula WHERE"""
        for table in self.LARGE_TABLES:
            # Buscar la tabla en FROM o JOIN
            if re.search(r'\b' + table.upper() + r'\b', sql_upper):
                # Verificar si hay WHERE
                if not re.search(r'\bWHERE\b', sql_upper):
                    self.warnings.append(
                        f"⚠️ RENDIMIENTO: La tabla '{table}' es grande y NO tiene "
                        f"cláusula WHERE. Esto puede causar lentitud."
                    )
                    self.suggestions.append(
                        f"Agrega un filtro WHERE para la tabla {table}, por ejemplo: "
                        f"WHERE {table[:5]}_Date >= '2024-01-01'"
                    )

    def _add_suggestions(self, sql: str):
        """Agrega sugerencias de mejora"""
        sql_upper = sql.upper()

        # Sugerir ORDER BY si no existe
        if 'ORDER BY' not in sql_upper:
            self.suggestions.append(
                "💡 Considera agregar ORDER BY para ordenar los resultados, "
                "por ejemplo: ORDER BY FechaCreacion DESC"
            )

        # Sugerir alias para tablas si hay múltiples FROM/JOIN
        join_count = sql_upper.count('JOIN')
        from_count = sql_upper.count('FROM')
        if join_count + from_count > 2:
            if not re.search(r'\bAS\s+\w+\b', sql_upper):
                self.suggestions.append(
                    "💡 Usa alias para las tablas (AS alias) para hacer "
                    "la consulta más legible."
                )

    def format_result(self, result: ValidationResult) -> str:
        """Formatea el resultado de validación para mostrar al usuario"""
        output = []

        if result.is_valid:
            output.append("✅ CONSULTA VÁLIDA - Puede ejecutarse de forma segura\n")
        else:
            output.append("❌ CONSULTA INVÁLIDA - NO puede ejecutarse\n")

        if result.errors:
            output.append("=" * 70)
            output.append("ERRORES CRÍTICOS (DEBEN CORREGIRSE):")
            output.append("=" * 70)
            for i, error in enumerate(result.errors, 1):
                output.append(f"{i}. {error}")
            output.append("")

        if result.warnings:
            output.append("=" * 70)
            output.append("ADVERTENCIAS (RECOMENDADO CORREGIR):")
            output.append("=" * 70)
            for i, warning in enumerate(result.warnings, 1):
                output.append(f"{i}. {warning}")
            output.append("")

        if result.suggestions:
            output.append("=" * 70)
            output.append("SUGERENCIAS DE MEJORA:")
            output.append("=" * 70)
            for i, suggestion in enumerate(result.suggestions, 1):
                output.append(f"{i}. {suggestion}")
            output.append("")

        return "\n".join(output)

def validate_sql_file(file_path: str) -> ValidationResult:
    """
    Valida un archivo SQL completo

    Args:
        file_path: Ruta al archivo SQL

    Returns:
        ValidationResult con el resultado de la validación
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            sql = f.read()

        validator = SQLValidator()
        result = validator.validate(sql)

        return result
    except FileNotFoundError:
        return ValidationResult(
            is_valid=False,
            errors=[f"❌ ERROR: Archivo no encontrado: {file_path}"],
            warnings=[],
            suggestions=[]
        )
    except Exception as e:
        return ValidationResult(
            is_valid=False,
            errors=[f"❌ ERROR al leer archivo: {str(e)}"],
            warnings=[],
            suggestions=[]
        )

# Ejemplos de uso
if __name__ == "__main__":
    print("=" * 80)
    print("VALIDADOR DE CONSULTAS SQL - TrakCare/ALMA")
    print("=" * 80)
    print()

    # Ejemplo 1: Consulta válida
    print("📝 EJEMPLO 1: Consulta VÁLIDA")
    print("-" * 80)
    sql_valid = """
    -- Consulta de pacientes hospitalizados
    SELECT TOP 100
        PA.PAADM_ADMNo AS NumeroEpisodio,
        P.PAPER_Name AS NombrePaciente,
        PA.PAADM_AdmDate AS FechaIngreso
    FROM SQLUser.PA_Adm PA
    INNER JOIN SQLUser.PA_PatMas PM ON PA.PAADM_PAPMI_DR = PM.PAPMI_RowId
    INNER JOIN SQLUser.PA_Person P ON PM.PAPMI_PAPER_DR = P.PAPER_RowId
    WHERE PA.PAADM_Type = 'I'
      AND PA.PAADM_DischgDate IS NULL
      AND PA.PAADM_AdmDate >= '2024-01-01'
    ORDER BY PA.PAADM_AdmDate DESC;
    """

    validator = SQLValidator()
    result = validator.validate(sql_valid)
    print(validator.format_result(result))

    # Ejemplo 2: Consulta inválida (sin TOP)
    print("📝 EJEMPLO 2: Consulta INVÁLIDA (sin límite)")
    print("-" * 80)
    sql_invalid = """
    SELECT *
    FROM SQLUser.PA_Adm
    WHERE PAADM_Type = 'I';
    """

    result = validator.validate(sql_invalid)
    print(validator.format_result(result))

    # Ejemplo 3: Consulta peligrosa (UPDATE)
    print("📝 EJEMPLO 3: Consulta PROHIBIDA (UPDATE)")
    print("-" * 80)
    sql_dangerous = """
    UPDATE SQLUser.PA_Person
    SET PAPER_Name = 'Test'
    WHERE PAPER_RowId = 1;
    """

    result = validator.validate(sql_dangerous)
    print(validator.format_result(result))
